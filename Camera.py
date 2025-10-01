from onvif import ONVIFCamera

class Camera:
    ip = None
    port = None
    user = None
    password = None
    
    onvif = None
    ptz_service = None
    media_service = None
    profile = None
    presets = None
    
    def __init__(self, ip=None, port=None, user=None, password=None):
        if ip:
            self.ip = ip
        if port:
            self.port = port
        if user:
            self.user = user
        if password:
            self.password = password
        self.connect()
        self.get_profile()
        self.get_presets()        

    def connect(self):
        try:
            self.onvif = ONVIFCamera(self.ip, self.port, self.user, self.password)
        except Exception as e:
            raise Exception(f"Erro ao conectar na câmera: {e}")
        
        self.ptz_service = self.onvif.create_ptz_service()
        self.media_service = self.onvif.create_media_service()
        
    def get_profile(self):
        self.profile = self.media_service.GetProfiles()[0]
        return self.profile

    def get_presets(self):
        self.presets = self.ptz_service.GetPresets({'ProfileToken': self.profile.token})
        return self.presets
    
    def move_to_preset(self, preset):
        self.ptz_service.GotoPreset({
            'ProfileToken': self.profile.token,
            'PresetToken': preset.token,
            'Speed': {
                'PanTilt': {'x': 0.5, 'y': 0.5},
                'Zoom': {'x': 0.5}
            }
        })