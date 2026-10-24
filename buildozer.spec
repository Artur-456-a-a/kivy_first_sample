[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.mykivyapp

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

# КЛЮЧЕВОЙ МОМЕНТ: используем master-версии для обхода багов Android 14/15
requirements = python3,kivy==master,https://github.com/kivymd/KivyMD/archive/master.zip,pillow

orientation = portrait
fullscreen = 0

# Настройки под новые Android (API 35), чтобы избежать крашей
android.api = 35
android.minapi = 23
android.ndk = 28c
android.ndk_api = 23

# Включаем сборку под 64-битную архитектуру (обязательно для Honor и новых устройств)
android.archs = arm64-v8a

# Разрешения (если нужны)
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
