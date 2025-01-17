# Script to set up tests on AppVeyor Windows.

$Dependencies = "PyYAML acstore artifacts dfdatetime dfimagetools dfvfs dfwinreg dtfabric idna libbde libcaes libcreg libevt libevtx libewf libexe libfcrypto libfsapfs libfsext libfsfat libfshfs libfsntfs libfsxfs libfvde libfwevt libfwnt libluksde libmodi libphdi libqcow libregf libsigscan libsmdev libsmraw libvhdi libvmdk libvsapm libvsgpt libvshadow libvslvm libwrc pytsk3 xattr"

If ($Dependencies.Length -gt 0)
{
	$Dependencies = ${Dependencies} -split " "

	$Output = Invoke-Expression -Command "git clone https://github.com/log2timeline/l2tdevtools.git ..\l2tdevtools 2>&1" | %{ "$_" }
	Write-Host (${Output} | Out-String)

	If ($env:APPVEYOR_REPO_BRANCH -eq "main")
	{
		$Track = "stable"
	}
	Else
	{
		$Track = $env:APPVEYOR_REPO_BRANCH
	}
	New-Item -ItemType "directory" -Name "dependencies"

	$env:PYTHONPATH = "..\l2tdevtools"

	$Output = Invoke-Expression -Command "& '${env:PYTHON}\python.exe' ..\l2tdevtools\tools\update.py --download-directory dependencies --machine-type ${env:MACHINE_TYPE} --track ${env:L2TBINARIES_TRACK} ${Dependencies} 2>&1" | %{ "$_" }
	Write-Host (${Output} | Out-String)
}

