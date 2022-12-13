[app]

title = test

package.name = test

package.domain = org.pythonlab

source.dir = .

source.include_exts = py,png,jpg,kv,atlas,txt,json,ttf

version = 0.0.2

requirements = kivy,https://github.com/kivymd/KivyMD/archive/master.zip,sdl2_ttf==2.20.1

requirements.source.kivymd = ../../kivymd

fullscreen = 0

p4a.branch = develop

#
# Android specific
#

android.permissions = INTERNET

android.api = 28

android.archs = armeabi-v7a


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
