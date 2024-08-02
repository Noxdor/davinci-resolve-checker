local_str = {
    "locale": "Verwende Sprachpaket",
    "project name": "DaVinci-Resolve-Checker",
    "you are running": "Du bist am Ausführen von",
    "script not tested on distro": "aber dieses Skript wurde nicht auf dieser Distro getestet.",
    "which DR package": "Installiertes DaVinci Resolve Paket:",
    "chassis": "Gehäusetyp:",
    "unsupported chassis": "Achtung: Dein Gehäusetyp wird von diesem Skript nicht unterstützt. Bitte erstelle ein Issue und melde deinen Gehäusetypen.",
    "Notebook": "Notebook",
    "Laptop": "Laptop",
    "Desktop": "Stand-PC",
    "openCL drivers": "Installierte OpenCL-Treiber:",
    "presented gpus": "Gefundene GPUs:",
    "kernel driver": "Verwendeter Kernel-Treiber:",
    "opengl vendor": "OpenGL-Herstellerkennung:",
    "missing opengl vendor": "Es war nicht möglich, die OpenGL-Herstellerkennung auszulesen. Es ist möglich, dass du versucht, AMD Pro OpenGL zu verwenden, obwohl deine Haupt-GPU von Intel ist. Es ist auch möglich, dass du das Skript via SSH ausführst.",
    "should uninstall opencl-mesa": "Du solltest opencl-mesa deinstallieren. Ansonsten verhält sich DR (v17.1.1) falsch: Image ist korrupt/beschädigt. Falls du die GPU-Option in den Einstellungen deaktivierst und DR neu startest, könnte deine ganze Desktopsitzung korrumpiert werden, sodass du deinen Rechner neu starten musst. Dies ist mindestens bei AMD-GPUs beobachtet worden.",
    "several intel gpus": "Du hast mehrere Intel-GPUs. Ich bin verwirrt. Nutzt du ein Motherboard mit Multi-CPU-Support? Oder Intel-iGPU + Intel-dGPU (was zum Zeitpunkt des Schreibens nicht existiert)?",
    "several amd gpus": "Du hast mehrere AMD-GPUs. DR Studio kann mehrere GPUs nutzen. Das Skript wird überprüfen, ob der richtige Treiber für deine rendernde GPU verwendet wird. Denk daran, dass, falls du 'prime offloading' nutzt, deine Primär-GPU immer noch die richtigen Treiber braucht (wird vom Skript nicht überprüft).",
    "several nvidia gpus": "Du hast mehrere Nvidia-GPUs. Ich bin verwirrt. Welche willst du verwenden?",
    "confused by nvidia and amd gpus": "Du hast AMD- und Nvidia-GPUs. Ich bin verwirrt. Welche willst du verwenden?",
    "only intel gpu, cannot run DR": "Du hast nur eine Intel-GPU. Aktuell kann DR keine Intel-GPUs für OpenCL verwenden. Du kannst DR nicht ausführen. Schau dir diesen Forumbeitrag für weitere Details an: https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=81579",
    "mixed intel and amd gpus": "Ich konnte bisher keine funktionierende Konfiguration für Laptops mit Intel + AMD-Grafikkarte finden. Und du?",
    "set primary display to PCIE": "Deine primäre GPU ist von Intel. Geh in deine UEFI-Einstellungen und stell das Hauptdisplay auf PCIE ein. Ansonsten kannst du DaVinci Resolve nicht verwenden (Ich habe es nicht getestet).",
    "switch from radeon driver to amdgpu": "Du verwendest aktuell die Radeon-Treiber. Wechsel zu amdgpu, wie hier beschrieben: https://wiki.archlinux.org/title/AMDGPU#Enable_Southern_Islands_(SI)_and_Sea_Islands_(CIK)_support. Ansonsten kannst du DaVinci Resolve nicht ausführen.",
    "no support for amd driver, cannot run DR": "Deine GPU unterstützt nur Radeon-Treiber. DaVinci Resolve benötigt 'amdgpu progl', was nur mit amdgpu-Treibern läuft. Du kannst DaVinci Resolve nicht ausführen.",
    "not running amdgpu driver, cannot run DR": "Aus irgendeinem Grund verwendest du nicht die amdgpu-Treiber. Du kannst DaVinci Resolve nicht ausführen.",
    "not using Pro OpenGL": "Du verwendest nicht die Pro-OpenGL-Implementierung. Installiere amdgpu-pro-libgl und führe DaVinci Resolve mit progl prexis aus. Ansonsten wird es crashen.",
    "missing opencl driver": "Du hast keine opencl-Treiber für deine AMD-GPU. Installiere diese, sonst kannst du DaVinci Resolve nicht verwenden.",
    "good to run DR": "Sieht gut aus! Du solltest DaVinci Resolve verwenden können.",
    "missing opencl-nvidia package": "Du hast das opencl-nvidia-Paket nicht installiert (oder ein alternatives Paket, welches opencl-nvidia zur Verfügung stellt). Installiere dieses, ansonsten kannst du DR nicht verwenden. Selbst wenn du planst, CUDA zu verwenden, ist opencl-nvidia als Abhängigkeit erforderlich.",
    "missing nvidia as kernel driver": "Du verwendest Nvidia nicht als Kernel-Treiber. Verwende die proprietären Nvidia-Treiber, sonst kannst du DaVinci Resolve nicht verwenden.",
    "not running nvidia rendered": "Du hast keinen aktiven Nvidia-Renderer. Versuche, das Skript mit 'prime-run' oder einer anderen Methode für Optimus auszuführen, ansonsten kannst du DaVinci Resolve nicht benutzen.",
    "opencl-amd and progl versions mismatch": "Achtung: opencl-amd (%s) und amdgpu-pro-libgl (%s) Versionen passen nicht zusammen.",
    "skipping vfio binded gpu": "Die GPU %s verwendet aktuell die vfio-pci-Treiber, sie wird bei den weiteren Checks übersprungen.",
    "amd codename undetectable": "Achtung: Deine GPU wurde nicht in der Codename-Liste gefunden. Es wird angenommen, dass es eine alte GPU ist, welche progl erfordert. Falls das stimmt, erstelle bitte ein Issue.",
    "not found any opencl-driver": "Kein Paket gefunden, welches opencl-Treiber bereitstellt.",
    "missing opencl-driver for amd": "Fehlender opencl-Treiber für AMD-GPU: Es ist empfohlen, rocm-opencl-runtime zu installieren.",
    "use rocm only instead of opencl-amd": "Das Paket opencl-amd enthält beide Implementationen für AMD: orca (legacy) und rocm (modern). DR crasht, falls es beide sieht (bisher noch kein Bug-Report). Und aktuell unterstützt der opencl-Loader noch nicht, ein ICD-File manuell zu bestimmen: https://github.com/OCL-dev/ocl-icd/issues/7#issuecomment-1522941979. Es ist empfohlen rocm-opencl-runtime anstatt opencl-amd zu installieren.",
    "use roc_enable_pre_vega or use pro stack": "Du solltest die Umgebungsvariable ROC_ENABLE_PRE_VEGA=1 setzen. Verwende ansonsten den pro-Stack (Führe das Skript mit --pro aus), da opencl (legacy) progl benötigt, um zu funktionieren.",
    "pro stack on modern gpu": "Achtung: Es gibt keinen Grund, den pro-Stack auf modernen GPUs zu verwenden.",
}
