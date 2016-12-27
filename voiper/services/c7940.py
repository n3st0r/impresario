template_c7940 = """
# SIP Configuration Generic File (start)

# Proxy Server
proxy1_address: "{{ sip_proxy }}"
proxy2_address: ""

# Line 1 Settings
line1_name: "{{ number1 }}"                ; Line 1 Extension - User ID
line1_displayname: "{{ number1 }}"         ; Line 1 Display Name
line1_authname: "{{ number1 }}"            ; Line 1 Registration Authentication
line1_password: "{{ secret1 }}" ; Line 1 Registration Password

# Line 2 Settings
line2_name: "{{ number2 }}"                      ; Line 2 Extension - User ID
line2_displayname: "{{ number2 }}"                   ; Line 2 Display Name
line2_authname: "{{ number2 }}"         ; Line 2 Registration Authentication
line2_password: "{{ secret2 }}"         ; Line 2 Registration Password


# Emergency Proxy info
proxy_emergency: ""
proxy_emergency_port: "5060"

# Backup Proxy info
proxy_backup: ""
proxy_backup_port: "5060"

# Outbound Proxy info
outbound_proxy: ""
outbound_proxy_port: "5060"

# NAT/Firewall Traversal
nat_enable: "0"
nat_address: ""
voip_control_port: "5060"
start_media_port: "16384"
end_media_port:  "32766"
nat_received_processing: "0"

# Phone Label (Text desired to be displayed in upper right corner)
phone_label: "{{ phone_label }}"            ; Has no effect on SIP messaging

# Time Zone phone will reside in
time_zone: UTC

# Telnet Level (enable or disable the ability to telnet into this phone
telnet_level: "0"      ; 0-Disabled (default), 1-Enabled, 2-Privileged

# Phone prompt/password for telnet/console session

phone_prompt: "{{ phone_prompt }}"                              ; Telnet/Console Prompt
phone_password: "{{ secret }}"                          ; Telnet/Console Password

# Enable_VAD (1-enabled, 0-disabled)
enable_vad: "0"

# Network Media Type (auto, full100, full10, half100, half10)
network_media_type: "auto"
user_info: phone

# URL for external Directory location
# URL for branding logo to be used on phone display
logo_url: "{{ logo_url }}"

# SIP Configuration Generic File (stop)

# Insert Extension for voice mail retrieval here, this is what's dialed when they hit the "envelope" key on the phone.
messages_uri:  "{{ messages_uri }}"

# This is a bitmap, and it's supposed to set line 6 for auto-answer.
#However it seems that the newer versions won't allow anything above line4 to be set to auto-answer via tftp.
auto_answer: 32
autocomplete: 0
dnd_control: 2

# Dialplan template (.xml format file relative to the TFTP root directory)
dial_template: voip/dialplan/otago
"""
