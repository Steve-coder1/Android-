[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example
source.dir = .                  # THIS LINE IS IMPORTANT
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = armeabi-v7a
