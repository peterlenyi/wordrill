# Changelog

## 1.0.6 (2025-07-27)

Bug: not parsing multiline values in dictionaries
- (fix) Append following values to the last key

Bug: raising intermittent import errors
- (fix) Use correct package in shell script

## 1.0.5 (2025-07-27)

Bug: raising intermittent import errors
- (fix) Place source code in a python package
- (fix) Use absolute imports in all modules
- (fix) Invoke main as a module in shell script

## 1.0.4 (2025-07-27)

Bug: not parsing comments in dictionaries
- (fix) Ignore line-level comments in dictionaries (# and ;)

## 1.0.3 (2025-07-27)

Bug: looking for dictionaries in wrong folders
- (fix) Look for dictionaries in the user config dir
- (fix) Use the OS-specific user config dir

## 1.0.2 (2025-07-27)

Bug: using wrong imports in test modules 
- (fix) Use absolute imports in test modules

## 1.0.1 (2025-07-27)

Bug: using wrong parser for translation dictionary
- (fix) Use the translation dictionary parser

## 1.0.0 (2025-07-14)

Wordrill 1.0.0
- (new) Print the copyright statement on startup
- (new) Prompt user for instructions in a loop
- (new) Exit the application on /exit command
- (new) Show the help text on /help command 
- (new) Start the test loop on /test command
- (new) Load dictionaries per selected locales in test loop
- (new) Switch to easy mode on /easy command in test loop
- (new) Switch to hard mode on /hard command in test loop
- (new) Pick a random translation from dictionary in test loop
- (new) Show user additional information about word when right
- (new) Show user possible translations of the word when wrong
- (new) Shell script
- (new) Unit test suite
- (new) OSS project files

___
<sup>Wordrill © 2025 by Peter Lényi is licensed under GNU GPL v3</sup>  
<sup>License: https://www.gnu.org/licenses/gpl-3.0.html </sup>  
<sup>Source: [O.Lacan: keep a changelog](https://keepachangelog.com/en/1.1.0/)<sup/>
