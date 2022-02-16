# i3
this is my i3wm config files  
created by blacksugar

## Introduction
+ **alacritty**  the terminal emulator
+ **rime** the input method
+ **i3** my window manager config files and scripts
+ **picom** for the transparent
+ **polybar** the status bar
+ **ranger** file manager
+ **Dank Mono** the font that I used in my system
+ **rofi** the window switcher

## 一些配置项记录

### wayland下启用ibus
`sudo vi /etc/environment`

```
INPUT_METHOD=ibus
GTK_IM_MODULE=ibus
QT_IM_MODULE=ibus
XMODIFIERS=@im=ibus
```
