# ball-clock
## Background
The ball clock is a simple device which keeps track of the passing minutes by moving ball-bearings through a series of rails and queues. Each minute, a rotating arm removes a ball bearing from the queue at the bottom, raises it to the top of the clock and deposits it on a track leading to indicators displaying minutes, five-minutes and hours. These indicators display the time between 1:00 and 12:59, but without 'a.m.' or 'p.m.' indicators. Thus 2 balls in the minute indicator, 6 balls in the five-minute indicator and 5 balls in the hour indicator displays the time 5:32.

Unfortunately, most commercially available ball clocks do not incorporate a date indication, although this would be simple to do with the addition of further carry and indicator tracks. However, all is not lost! As the balls migrate through the mechanism of the clock, they change their relative ordering in a predictable way. Careful study of these orderings will therefore yield the time elapsed since the clock had some specific ordering. The length of time which can be measured is limited because the orderings of the balls eventually begin to repeat. Your program must compute the time before repetition, which varies according to the total number of balls present.
 
## Operation of the Ball Clock
Every minute, the least recently used ball is removed from the queue of balls at the bottom of the clock, elevated, then deposited on the minute indicator track, which is able to hold four balls. When a fifth ball rolls on to the minute indicator track, its weight causes the track to tilt. The four balls already on the track run back down to join the queue of balls waiting at the bottom in reverse order of their original addition to the minutes track. The fifth ball, which caused the tilt, rolls on down to the five-minute indicator track. This track holds eleven balls. The twelfth ball carried over from the minutes causes the five-minute track to tilt, returning the eleven balls to the queue, again in reverse order of their addition. The twelfth ball rolls down to the hour indicator. The hour indicator also holds eleven balls, but has one extra fixed ball which is always present so that counting the balls in the hour indicator will yield an hour in the range one to twelve. The twelfth ball carried over from the five-minute indicator causes the hour indicator to tilt, returning the eleven free balls to the queue, in reverse order, before the twelfth ball itself also returns to the queue.
 
## Input
The input defines a succession of ball clocks. Each clock operates as described above. The clocks differ only in the number of balls present in the queue at one o'clock when all the clocks start. This number is given for each clock, one per line and does not include the fixed ball on the hours indicator. Valid numbers are in the range 27 to 127. A zero signifies the end of input.
 
## Output
For each clock described in the input, your program should report the number of balls given in the input and the number of days (24-hour periods) which elapse before the clock returns to its initial ordering.

Sample Input | Sample Output
------------ | -------------
30 | 15 days
45 | 378 days

## Requirements
1. Use the language of your own choice to solve for any input between 27 to 127. For example C#, JavaScript, Ruby, Go, or Python.
1. Provide automated unit and integration tests for your solution.
1. Provide a Dockerfile to build a Docker Image that encapsulates your solution.
1. Provide a single command to build and test your solution on a fresh clone of the repo.
1. Provide a way for users to provide an input value
1. You must use git for source control and prior to the second interview please push your code to github.com and send me the link to your repository.
1. Be prepared to answer a question along the lines of… How would your code change if given the requirement to add a new queue or alter existing queues? Would you be required to add new code, or modify existing code?

### Clone the repo using the following command
git clone https://github.com/keldwud/ball-clock.git

### Build using the following command from the cloned repo
docker build -t keldwud/ball-clock .

### Run using the following command
docker run ball-clock clock _number_ # where number is a number from 27 - 127

Output will be in the format:
