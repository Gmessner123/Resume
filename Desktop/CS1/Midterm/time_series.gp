set title "r = 0.4" font ",24"
set nokey
set style line 1 lc rgb 'blue' pt 6 ps 1.5
plot "time_series" using 1:2 with linespoints ls 1
pause -1 "hit any key to continue..."

set title "r = 1.9" font ",24"
set nokey
set style line 1 lc rgb 'blue' pt 6 ps 1.5
plot "time_series" using 1:3 with linespoints ls 1
pause -1 "hit any key to continue..."

set title "r = 2.5" font ",24"
set nokey
set style line 1 lc rgb 'blue' pt 6 ps 1.5
plot "time_series" using 1:4 with linespoints ls 1
pause -1 "hit any key to continue..."

