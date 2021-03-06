#!/bin/bash
case $1 in
        init)
                for i in 7 15 0 1 3 4 13 6; do
                        wiringPi-gpio mode $i output
                        wiringPi-gpio write $i 0
                done
        ;;

        b)
                wiringPi-gpio write 4 1;
        ;;
        nob)
                wiringPi-gpio write 4 0;
        ;;
        cw)
                wiringPi-gpio write 0 0;
                wiringPi-gpio write 1 1;
        ;;
        ccw)
                wiringPi-gpio write 0 1;
                wiringPi-gpio write 1 0;
        ;;
        noh)
                wiringPi-gpio write 0 0;
                wiringPi-gpio write 1 0;
        ;;
        up)
                wiringPi-gpio write 7 1;
                wiringPi-gpio write 15 0;
        ;;
        down)
                wiringPi-gpio write 7 0;
                wiringPi-gpio write 15 1;
        ;;
        nov)
                wiringPi-gpio write 7 0;
                wiringPi-gpio write 15 0;
        ;;
        led)
                wiringPi-gpio write 6 1;
        ;;
        noled)
                wiringPi-gpio write 6 0;
        ;;

        *)
                echo "all OFF!"
                for i in 7 15 0 1 3 4; do
                        wiringPi-gpio write $i 0
                done
        ;;
esac
