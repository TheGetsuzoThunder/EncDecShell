import base64, codecs
magic = 'IyBjb2Rpbmc6IHV0Zi04DQoNCmltcG9ydCBvcw0KaW1wb3J0IHN5cw0KaW1wb3J0IGZpbGVpbnB1dA0KDQpOID0gJ1wwMzNbMG0nDQpEID0gJ1wwMzNbOTBtJw0KVyA9ICdcMDMzWzE7MzdtJw0KQiA9ICdcMDMzWzE7MzRtJw0KUiA9ICdcMDMzWzE7MzFtJw0KRyA9ICdcMDMzWzE7MzJtJw0KWSA9ICdcMDMzWzE7MzNtJw0KQyA9ICdcMDMzWzE7MzZtJw0KDQphc2sgPSBXICsgJ1snICsgQiArICc/JyArIFcgKyAnXSAnDQpzdWtzZXMgPSBXICsgJ1snICsgRyArICfiiJonICsgVyArICddICcNCmVyb3IgPSBXICsgJ1snICsgUiArICchJyArIFcgKyAnXScNCg0KYmFubmVyID0gIiIiDQovLyAgIC8gLyAgICAgICAgICAgICAgICAgIC8vICAgKSApICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgIC8vX18gICAgICBfICAgICAgX18gICAoKCAgICAgICAgLyBfICAgICAgX18gICAgIC8vIC8vICANCiAgLyBfXyAgICAvLyAgICkgKSAvLyAgICkgKSAgXFwgICAgIC8vICAgKSApIC8vXykgKSAvLyAvLyA'
love = 'tVN0XVP8iVPNtVPNtVPNiYlNtVP8tYlNiYlNtVPNtVPNtVPNtXFNcVP8iVPNtYlNiVP8iVPNtVPNtVP8iVP8iVPNtVN0XYl9sYlNiVP8iVPNtYlNiVPtbKlNbXS8tYlNiVP8iVPNtYlNiVPtbK18tVPNiYlNiYj0XJmSqVRIhLlOoZy0tETIwQDbvVvVhMz9loJS0XRDfIlkRYSpfEPkKYSxfIlkRYSpfEPkKYRDfIlkRYSpfEPkMYRDfIlkRYSxfEPkUYSpfElkRYRpfIlkUYSxfEPkMYRDfJFkRYSxfEPkMXD0XQDcvLJ5hMKVlVQ0tVvVvQDbtVPOPrFOHnUIhMTIlQDbvVvVhMz9loJS0XRpfIlkUYSpfElkKYRpfIlxAPt0XpUWcoaDtLzShozIlQDcjpzyhqPOvLJ5hMKVlQDbAPzEyMvOxMJglnKNbXGbAPvNtVUElrGbAPvNtVPNtVPOmLlN9VUWuq19coaO1qPuup2ftXlOKVPftVyAwpzyjqPNvVPftDvNeVPV+VPVtXlOKXD0XVPNtVPNtVTLtCFOipTIhXUAwYPqlWlxAPvNtVPNtVPOznJkyMTS0LFN9VTLhpzIuMPtcQDbtVPNtVPNtMv5woT9mMFtcQDbAPvNtVPNtVPOhMKqxLKEuVQ0tMzyfMJEuqTRhpzIjoTSwMF'
god = 'giYmFzZTY0IiwidGh1bmRlciIpDQoNCiAgICAgICBvdXQgPSByYXdfaW5wdXQoYXNrICsgVyArICJPdXRwdXQiICsgQiArICIgPiAiICsgVykNCiAgICAgICBmID0gb3BlbihvdXQsJ3cnKQ0KICAgICAgIGYud3JpdGUobmV3ZGF0YSkNCiAgICAgICBmLmNsb3NlKCkNCg0KICAgICAgIG9zLnN5c3RlbSgidG91Y2ggdGVzLnNoIikNCiAgICAgICBvcy5zeXN0ZW0oImJhc2ggIiArIG91dCArICIgPiB0ZXMuc2giKQ0KICAgICAgIG9zLnJlbW92ZShvdXQpDQogICAgICAgb3Muc3lzdGVtKCJtdiAtZiB0ZXMuc2ggIiArIG91dCkNCiAgICAgICBwcmludCAoc3Vrc2VzICsgIlN1a3Nlcy4uIikNCg0KICAgZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0Og0KICAgICAgIHByaW50IChlcm9yICsgIiBEaWhlbnRpa2FuISIpDQogICBleGNlcHQgSU9FcnJvcjoNCiAgICAgICBwcmludCAoZXJvciArICIgRmlsZSBnYSBhZGEiKQ0KDQpkZWYgZW5rcmlwKCk6DQogICB0cnk6DQogICAgICAgc2NyaXB0ID0gcmF3X2luc'
destiny = 'UI0XTSmnlNeVSptXlNvH2AlnKO0VPVtXlOPVPftVw4tVvNeVSpcQDbtVPNtVPNto3I0pUI0VQ0tpzS3K2yhpUI0XTSmnlNeVSptXlNvG3I0pUI0VPVtXlOPVPftVw4tVvNeVSpcQDbtVPNtVPNto3Zhp3ymqTIgXPWvLKAbYJ9vMaImL2S0MFNvVPftp2AlnKO0VPftVvNgolNvVPfto3I0pUI0VPxAPvNtVPNtVPOjpzyhqPNbp3Iep2ImVPftVxEiozHhYvVcQDbtVPOyrTAypUDtF2I5Lz9upzEWoaEypaW1pUD6QDbtVPNtVPNtpUWcoaDtXTIlo3VtXlNvVREcnTIhqTyeLJ4uVvxAPvNtVTI4L2IjqPOWG0Ilpz9lBt0XVPNtVPNtVUOlnJ50VPuypz9lVPftVvOTnJkyVTquVTSxLFVcQDbAPt0XoJIhqFN9VUWuq19coaO1qPuKVPftVyOcoTybVT1yoaHvVPftDvNeVPVtCvNvXD0XQDccMvOgMJ51VQ09VPVkVvOipvOgMJ51VQ09VPVjZFV6QDbtVPOyozglnKNbXD0XMJkcMvOgMJ51VQ09VPVlVvOipvOgMJ51VQ09VPVjZvV6QDbtVPOxMJglnKNbXD0XMJkmMGbAPvNtVUOlnJ50VPuypz9lVPftVyyaVRWyozIlVvx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
