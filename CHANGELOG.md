# Changelog

## 1.0.5 (2025-07-27)

Fix: raising intermittent import errors
- (app) Place source code in a python package
- (fun) Use absolute imports in all modules
- (app) Shell script invokes main as a module

## 1.0.4 (2025-07-27)

Fix: not parsing comments in dictionaries
- (fun) Ignore line-level comments in dictionaries (# and ;)

## 1.0.3 (2025-07-27)

Fix: looking for dictionaries in wrong folders
- (fun) Look for dictionaries in the user config dir
- (fun) Use the OS-specific user config dir

## 1.0.2 (2025-07-27)

Fix: using wrong imports in test modules 
- (fun) Use absolute imports in test modules

## 1.0.1 (2025-07-27)

Fix: using wrong parser for translation dictionary
- (fun) Use the translation dictionary parser

## 1.0.0 (2025-07-14)

New: Wordrill 1.0.0
- (fun) Print the copyright statement on startup
- (fun) Prompt user for instructions in a loop
- (fun) Exit the application on /exit command
- (fun) Show the help text on /help command 
- (fun) Start the test loop on /test command
- (fun) Load dictionaries per selected locales in test loop
- (fun) Switch to easy mode on /easy command in test loop
- (fun) Switch to hard mode on /hard command in test loop
- (fun) Pick a random translation from dictionary in test loop
- (fun) Show user additional information about word when right
- (fun) Show user possible translations of the word when wrong
- (app) Shell script
- (app) Unit test suite
- (doc) OSS project files

___
<sup>Wordrill © 2025 by Peter Lényi is licensed under GNU GPL v3</sup>  
<sup>License: https://www.gnu.org/licenses/gpl-3.0.html </sup>  
<sup>Source: [O.Lacan: keep a changelog](https://keepachangelog.com/en/1.1.0/)<sup/>
