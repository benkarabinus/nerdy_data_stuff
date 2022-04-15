#!/bin/bash
# Ben Karabinus COMP 4447 Assignment 3 University of Denver Spring term 2022
# Bash script to calculates the MAX, MIN, MEDIAN and MEAN of the word frequencies in the
# file the  https://www.gutenberg.org/files/58785/58785-0.txt

if [ $# -lt 1 ]
   then
       echo "Please provide a txt file url"
       echo "usage ./calculate_basic_stats.sh  url"
       #exit with error
       exit 1
fi

echo  "############### Statistics for file  ############### "

# Q1(.5 point) write  positional parameter after echo to print its value. It is the file url used by curl command.

echo $1

# sort based on multiple columns
#Q2(2= 1+1 for right sorting of each columns). Write last sort command options so that first column(frequencies) is
#sorted via numerical values and
#second column is sorted by reverse alphabetical order

sorted_words=`curl -s $1|tr [A-Z] [a-z]|grep -oE "\w+"|sort|uniq -c|sort -k 1 -n -k 2 -r`
total_uniq_words=`echo "$sorted_words"|wc -l`
echo "Total number of words = $total_uniq_words"


#Q3(1=.5+.5 points ) Complete the code in the following echo statements to calculate the  Min and Max frequency with respective word
#Hint:  Use sorted_words variable, head, tail and command susbtitution

minFreq=`echo "$sorted_words"|tail -1`
maxFreq=`echo "$sorted_words"|head -1`
echo "Min frequency and word: $minFreq"
echo "Max frequency and word: $maxFreq"


#Median calculation

#Q4(2=1(taking care of even number of frequencies)+1 points(right value of median)). Using sorted_words,
#write code for median frequency value calculation. Print the value of the median with an echo statement, stating
# it is a median value.
#Code must check even or odd  number of unique words. For even case median is the mean of middle two values,
#for the odd case, it is middle value in sorted items.

n=$total_uniq_words

if [ $(($n % 2)) -eq 0 ]
then

    idx1=$(($n/2))
    idx2=$(($n/2+1))
    val1=$(echo "$sorted_words"|head -n $idx1|tail -1|grep -Eo '[0-9]')
    val2=$(echo "$sorted_words"|head -n $idx2|tail -1|grep -Eo '[0-9]')
    medianVal=$(echo $((($val1+$val2)/2)))
    echo "The median value of word frequencies is $medianVal"

else
    
    idx=$((($n+1)/2))
    medianVal=$(echo "$sorted_words"|head -n $idx|tail -1|grep -Eo '[0-9]')
    echo "The median value of word frequencies is $medianVal"
    
fi


# Mean value calculation
#Q5(1 point) Using for loop, write code to update count variable: total number of unique words
#Q6(1 point) Using for loop, write code to update total_freq variable : sum of frequencies
total_freq=0
count=0
col1=$(echo "$sorted_words"| grep -o  -E '^\s*[0-9]+')
for num in $col1
do
    let count++
    let total_freq+=num
done


#Q7(1 point) Write code to calculate mean frequency value based on total_freq and count
mean=$(($total_freq/$count))

echo "Sum of frequencies = $total_freq"
echo "Total unique words = $count"
echo "Mean frequency using integer arithmetics = $mean"

#Q8(1 point) Using bc -l command, calculate mean value.
# Write your code after = 
floatingPoint=$(echo "scale=4;$total_freq/$count" | bc)
echo "Mean frequency using floating point arithemetics (four units of precision) = $floatingPoint"


# Q9 (1 point) Complete lazy_commit bash function(look for how to write bash functions) to add, commit and push to the remote master.
# In the command prompt, this function is used as
#
# lazygit file_1 file_2 ... file_n commit_message
#
# This bash function must take files name and commit message as positional parameters
# and perform followling git function
#
# git add file_1 file_2 .. file_n
# git commit -m commit_message
# git push origin master

# Side: In the Linux if we put this function in .bashrc hidden file in
# the user home directory(type cd ~ to go to the home directory) and source .bashrc after adding this function,
# lazy_commit should be available in the command prompt.
# One can type lazy_commit file1 file2 ... filen  commit_message
# and file will be added , commited and pushed to remote master using one lazy_commit command.

# NOTE for grading!
# This function requires creation of dummy files for proper testing
# Files which do not exist will not be staged for commit, but will instead be considered part of commit message
# git commands will be echoed for purposes of testing. uncomment live git commands for push

echo "The first file" > file1.txt
echo "The second file" > file2.txt
echo "The third file" > file3.txt

function lazy_commit {

    files=""
    message=""
    for word in $*
    do
        if [[ -f $word ]];
        then 
            files+=" "
            files+=$word
        else
            message+=" "
            message+=$word
        fi
    done
    # live git commands below
    #git add $files
    #git commit -m $message
    #git push origin master
    #  echo git commands for testing purposes
    echo "git add" $files
    echo "git commit -m" $message
    echo "git push origin master" 
}

# function call for testing
echo "The lazy_commit function is called within the script for testing"
lazy_commit "file1.txt file2.txt file3.txt commit some stuff to the repo"