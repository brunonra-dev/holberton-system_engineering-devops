#0x02. Shell, I/O Redirections and filters

##Used Commands

###echo

echo print characters

###wc -l

Print the newline counts

###ls -t | head -n 10

show newst 10 files

###sort -d | uniq -u

sorted and unique lines

###cat /etc/passwd | grep -e bin | wc -l

count lines with bin

###cat /etc/passwd | grep -e root -A 3

show 3 lines after root pattern

###cat /etc/ssh/sshd_config | grep -i -e a

### cat /etc/ssh/sshd_config | grep -e ^[Aa-Zz]

###rev

reverse its input
