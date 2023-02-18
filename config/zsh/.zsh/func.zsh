# environment variables
export DS_HOST="u25@csci.cs.smu.ca"
export OS_HOST="os52@os.cs.smu.ca"
export STUD_HOST="u49@stud.cs.smu.ca"
export UGDEV="s_saad@ugdev.cs.smu.ca"
export UGDEV_HOME="s_saad@ugdev.cs.smu.ca:/home/students_tg21f/s_saad"
# export PATH="/opt/homebrew/opt/coreutils/libexec/gnubin:/opt/homebrew/opt/findutils/libexec/gnubin:$PATH"

# system
alias python="python3"
alias cutefetch="~/.local/bin/cutefetch"
alias cf="cutefetch"
alias fetch="neofetch"
alias clr="clear"
alias cat="bat -pP"
alias x="exit"
alias mkdir="mkdir -p"
alias ls="ls --color=auto -lh"
alias cp="rsync -ra --progress"
alias grep="grep --color -E"
alias pls="sudo"
alias lsblk="diskutil list"
alias fm=". ranger"
alias lock="osascript -e 'tell application \"System Events\" to keystroke \"q\" using {command down,control down}'"

# package management
alias yin="brew install"
alias yang="brew info"
alias wuji="brew uninstall"
alias see="brew search"
alias yup="brew upgrade"

pip() {
    if [ $1 = "search" ]; then
        pip_search "$2"
    else
	      pip3 "$@"
    fi
}

# utility
alias vim="nvim"
alias zrc="source ~/.zshrc"
alias edit="nvim"
alias edit-cf="nvim ~/.local/bin/cutefetch"
alias edit-fm="nvim ~/.config/ranger/"
alias edit-zrc="nvim ~/.zshrc"
alias edit-zfunc="nvim ~/.zsh/func.zsh"
alias edit-vrc="nvim ~/.config/nvim/lua/user/init.lua"
alias edit-wm="nvim ~/.config/yabai/yabairc"
alias edit-key="nvim ~/.config/skhd/skhdrc"
alias edit-prompt="nvim ~/.zsh/zen/prompt_zen_setup"
alias edit-yt="edit $(which yt)"
alias re-key="brew services restart skhd"
alias re-wm="launchctl kickstart -k 'gui/${UID}/homebrew.mxcl.yabai'"
alias up-wm="brew services stop yabai && brew upgrade yabai && sudo yabai --uninstall-sa && sudo yabai --install-sa && brew services start yabai"
alias py="ptpython"
alias dssh="ssh $DS_HOST"
alias ugsh="ssh $UGDEV"
alias ossh="ssh $OS_HOST"
alias studsh="ssh $STUD_HOST"
alias pyserve="python3 -m http.server 2021 -b 140.184.181.165 -d ./"
alias nf="netlify"
alias markd="cd ~/Library/Application\\ Support/marktext/themes/export/"
alias resumed="cd ~/Documents/Git/resume/"
alias cdfm="cd ~/.config/ranger/"
alias gitd="cd ~/Documents/Git/"
alias ytdir="cd ~/Documents/Git/ytplay/"
alias re="fuck"
alias nbpdf="jupyter nbconvert --to pdf"
alias weather="curl wttr.in"
alias twlartconfig="edit ~/Games/3DS-CFW/Downloads/TwilightBoxart-MacOS-CLI/TwilightBoxart.ini"
alias gcc="/opt/homebrew/bin/gcc-12"

utmount() {
    diskutil unmountDisk /dev/$1
    sudo diskutil mountDisk -mountPoint ~/Library/Containers/com.utmapp.UTM/Data/Documents /dev/$1
}

antlrc() {
    antlr "$1.g4"
    javac $1*.java
    echo Compilation Done. Enter expressions:
    grun "$1" prog -gui
}

epub2pdf() {
    ebook-convert "$1.epub" "$1.pdf"
}

sdcheck() {
    printf "Checking write speed and capacity...\n\n"
    f3write "/Volumes/$1"

    printf "\nChecking read speed and capacity...\n\n"
    f3read "/Volumes/$1"

    printf "\nAll checks completed!\n"
}

twlboxart() {
    dir="$PWD"
    cd ~/Games/3DS-CFW/Downloads/TwilightBoxart-MacOS-CLI
    ./TwilightBoxart.CLI
    cd $dir
}

source ~/.zsh/vn.zsh

etch() {
  case "$1" in
    "" | "-h" | "--help")  echo USAGE: etch \"disk\" \"iso_file\" ;;
    *)  sudo dd bs=4M if=$2 of=/dev/$1 status=progress oflag=sync ;;
  esac
}

lang() {
  curl cht.sh/$1/$(echo $2 | tr " " "+")
}

gitsync() {
  if [[ -n "$1" ]]; then
    msg="$1"
  else
    printf "Enter commit message: "
    read msg
  fi
  git add . && git commit -m "$msg" && git pull && git push
}

n()
{
    # Block nesting of nnn in subshells
    if [ -n $NNNLVL ] && [ "${NNNLVL:-0}" -ge 1 ]; then
        echo "nnn is already running"
        return
    fi

    # The behaviour is set to cd on quit (nnn checks if NNN_TMPFILE is set)
    # If NNN_TMPFILE is set to a custom path, it must be exported for nnn to
    # see. To cd on quit only on ^G, remove the "export" and make sure not to
    # use a custom path, i.e. set NNN_TMPFILE *exactly* as follows:
    #     NNN_TMPFILE="${XDG_CONFIG_HOME:-$HOME/.config}/nnn/.lastd"
    export NNN_TMPFILE="${XDG_CONFIG_HOME:-$HOME/.config}/nnn/.lastd"

    # Unmask ^Q (, ^V etc.) (if required, see `stty -a`) to Quit nnn
    # stty start undef
    # stty stop undef
    # stty lwrap undef
    # stty lnext undef

    nnn "$@"

    if [ -f "$NNN_TMPFILE" ]; then
            . "$NNN_TMPFILE"
            rm -f "$NNN_TMPFILE" > /dev/null
    fi
}

# sync Visual Novel project
vnsync() {
  dir="$PWD"

  # sync source files to git remote
  cd ~/Documents/RenPy\ Projects/Kwe
  echo "Uploading source files to remote Git repository..."
  gitsync
  
  # copy build file from build directory to target directory
  printf "\nCopying files from build directory...\n"
  cp -rf ~/Documents/RenPy\ Projects/Kwe-1.0-dists/Kwe-1.0-web/* ~/Documents/RenPy\ Projects/Kwe-1.0-dists/Kwe-story/
  printf "Files copied to target directory.\n\n"
  
  # sync build files to git remote
  cd ~/Documents/RenPy\ Projects/Kwe-1.0-dists/Kwe-story
  echo "Uploading build files to remote Git repository..."
  gitsync "updated build"

  # sync files to the server
  printf "\nUploading files to ugdev...\n\n"
  scp -r ~/Documents/RenPy\ Projects/Kwe-1.0-dists/Kwe-story/* group18@ugdev.cs.smu.ca:/home/groups_2021/group18/public_html/
  printf "\nFiles uploaded.\n\n"
  cd "$dir"
}

# copy files to and from ugdev.smu.ca SFTP server
ugcp() {
  server_path="$UGDEV"
  [[ -z "$2" ]] && from="$1" && to="$server_path" || from="$server_path/$2" && to="/Users/sage/Public/"
  [[ -d "$from" ]] && flags="-r" || flags=""
  scp "$flags" "$from" "$to"
}

ugsync() {
  scp -r ~/Documents/SMU/CSCI-2356/* s_saad@ugdev.cs.smu.ca:/home/students_tg22w/s_saad/public_html/
}

# compile fortran
gfc() {
  if [ -z "$1" ]; then
      echo "No input file."
  else
      fname="$(echo $1 | cut -d '.' -f1)"
      gfortran "$1" -o "$fname"
      "./$fname"
      rm "./$fname"
  fi
}

# call java using specified jdk version (16 by default)
jx() {
  case "$1" in
     8)
         JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.8.0_111.jdk/Contents/Home"
         ;;
     11)
         JAVA_HOME="/Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home"
         ;;
     *)
         JAVA_HOME="/Library/Java/JavaVirtualMachines/temurin-16.jdk/Contents/Home"
         ;;
  esac
  
  export JAVA_HOME; shift
  PATH=${JAVA_HOME}/bin:$PATH
  $*
}

