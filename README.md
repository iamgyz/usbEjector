# usbEjector

Anti-Hacking! Prevent someone from stealing your data via usb drive!

Automatically eject the usb storage when the usb device plugin your PC!

This is a python programming that can protect your PC! It won't allow any USB storage to plugin into your PC.

When there is a usb storage plugin, it would immediately safely remove the drive using PowerShell.

## Environment  
Because we've used PowerShell for ejection, so
Win7 or later version is required!

For example, if we want to remove the usb storage drive on F:\
```ps
$driveEject = New-Object -comObject Shell.Application
$driveEject.Namespace(17).ParseName("F:").InvokeVerb("Eject")
```

## Usage
`python3 usb_eject.py`  

