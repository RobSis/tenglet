TENGlet
=======

What is it?
-----------

'TENGlet' is program that creates large characters out of ordinary screen
 characters

```

                            .dP'      `Yb                
                    db    dP'          88          db    
                                       88                
   `Y8888888b.`YbanmmnmdP' 'Yb         88.d88b. .d8P"7b. 
      .dP'      dY     88   88         88P'  Y8 8'   `Yb 
    ,dP         Y8    .88   88         88    8P Yb.'  88 
    88     .    `Y888P'88  .8P        .88  bdP      .dP  
    `Yb...dP           88                         .dP'   
      `"""'            88                       .dP'  (like this)
                       Y8.
```

If it sounds familiar, than you probably know about FIGlet.
FIGlet is great tool, which I don't want to replace with my poor code.
This program was written mainly for tengwar typing and doesn't feature
FIGlet's enhancements like smushing, line wrapping, direction of text 
and others.

Why didn't I use figlet, then? When you want to type i.e. 'la', 
you print the letter 'l' first and then you print the 'a' sign above 
the previous letter. FIGlet can't do that (afaik)

But this project is mainly about the font file.
It is heavily based on Belinda Asbell's figlet font, which is great, but
unsuitable for serious tengwar typing, because many tengwar, tehtar and various
other signs and curls are missing. My font contains full Daniel S. Smith's
keymapping, which is respected as standard in tengwar coding.

Format of file
--------------
If you like this idea and want to contribute to ascii world, make another
font! Format is very easy.

First line is header:

```
tlf HEIGHT MAX_WIDTH
```

than characters follows. Each character is defined by header and body.
Header is:

```
(. || alt/(0-255)]) LEFT_SHIFT [*]
```

for example:

```
alt/0032 0 #space
j 0 #lambe
```

Body of character follows. It's just HEIGHT*line ended with '@' sign.
No empty lines are allowed in font file.

Input
-----
Unless you remember all keys from Dan Smith's keymapping, you will need
transcriber. There is plenty of them on net. For example:

* oTT - http://tengwar.art.pl/tengwar/ott/english.php
     which runs online.

* YaTT - http://linux.fjfi.cvut.cz/~nemec/tengwar/
     from my beloved home country :)

* Tengwar Scribe - http://at.mansbjorkman.net/tengscribe.htm
     best known. Check also ModeEditor.

* TENG http://tengwarformal.limes.com.pl/teng/
     my personal favorite. It is text filter (same as my program) and supports TengScribe modes.
