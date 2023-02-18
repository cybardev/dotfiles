export VNDEV="group18@ugdev.cs.smu.ca"

alias test-serve="python3 -m http.server 2021 -b 140.184.181.165 -d '/Users/sage/Documents/RenPy Projects/KLOQOWEJ-1.0-dists/KLOQOWEJ-1.0-web/'"

serve() {
  nohup python3 -m http.server 2021 -b 140.184.181.165 -d '/Users/sage/Documents/RenPy Projects/KLOQOWEJ-1.0-dists/KLOQOWEJ-1.0-web/' &
  eval "echo \$! > ~/.vn_pid"
}

killserve() {
  kill "$(cat ~/.vn_pid)"
}

