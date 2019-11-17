# README

This is an simple API of the website **[cn.buddymojo.com](http://cn.buddymojo.com).**

# Command Line Usage

Program itself can be run on the command line window.

If your running on linux, `python` won't work since this API is written in python 3. Try `python3` instead.

## Single Mode

Send message(s) to a single target. Type:

    python BuddyMojoAPI.py -s -T [target] -t [times] -n [name] [-l]

`-l` will show the url of the target

## Multiple Mode

Send messages to multiple target. Type:

    python BuddyMojoAPI.py -m -r [start] [end] -n [name]

The `start` and `end` is the userQuizId range.

# Examples

    python BuddyMojoAPI.py -s -T 296688 -t 3 -n hi -l

Will have the result like this:

![](https://i.imgur.com/APBT8fM.png)

The top 3 is the result.