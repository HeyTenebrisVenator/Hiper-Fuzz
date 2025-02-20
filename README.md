# Hiper-Fuzz
Hiper fuzz is a script that will help you at your fuzz step. It's made with python, and it only works in linux

*HOW TO INSTALL IT?*

To install, you can run the install.py command

```sudo python3 install.py```

# *HOW IT WORKS?*

The Hiper Fuzz is a tool that has a GUI made with tkinter. It was made with the purpose to be like dirbuster, but with some nem functionalitites

To run, you can, after running the installation, run the command:

```sudo hiper_fuzz```

After this, a GUI will spawn

![Captura de tela de 2025-02-19 12-57-59](https://github.com/user-attachments/assets/d1736885-c3b4-4b06-8c33-330c14430047)

To run, you need to specify a URL to start fuzzing.

After you put the name in the input and pressed enter, you select the wordlist.

There are 13 default wordlists to choose:


*Common list*

*big list*

*Apache*

*Common CVEs*

*IIS*

*Tomcat*

*Oracle*

*frontpage*

*ASPX*

*Graphql*

*Web Logic*

*Logins Fuzz*

*Common API endpoints*

# EXTRA FUNCTIONALITIES

You can set some others configurations, such as:

*Cookies* - You can set your own cookie to enter in the website

*Headers* - You can set a new Header. To put more you can separate them with comas (EX: Header:Value)

*Rate Limit* - This can be used to bypass some types of firewalls. You specify the maximum number of requests per second

*Save Output* - Is the location were you want to save your output

When you start a new fuzz, a terminal with ffuf running will appear.

# HOW TO ADD NEW WORDLISTS?

The hiper fuzz allow you to put your own wordlist. 

To do this, run the script:

```sudo python3 add_wordlist.py```

A interaction will start, asking you the location of the wordlist, and a name.
