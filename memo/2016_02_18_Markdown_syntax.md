# About Markdown Syntax

标签（空格分隔）： 未分类

---

I've used markdown to write document for some time, but haven't give much thought to it, just take it as a fashion.

Tonight, when I want to go over some of the markdown syntax, and found the origin of [Markdown: Syntax] [], which states the philosophy from designer, he wants it to be as easy-to-read and easy-to-write as is feasible. And the biggest source of inspiration of Markdown's syntax is the format of plain text email.

Raw HTML isn't reader friendly.

[Markdown: Syntax]:http://daringfireball.net/projects/markdown/syntax

#Syntax

##1. HEADERS
There are two header styles: *Setext* and *atx*.  

1.1 **Setext**

		This is an H1
		====

		This is an H2
		---
		
1.2 **atx**

	    # This is an H1
	    ## This is H2
	    ### This is H3

##2. PARAGRAPHS AND LINE BREAKS

    A paragraph is simply one or more consecutive lines of text, separated by one or more blank lines.
    
##3. BLOCKQUOTES

    > >This is a demo
    > of block
    > quote

> >This is a demo
> of block
> quote

##4. LISTS
    Markdown supports ordered (numbered) and unordered (bulleted) lists.

1. ordered
        1. xxx
        2. xxx
        3. xxx
    
2. unordered 
        * xxx
        * xxx
        * xxx

##5. CODE BLOCKS
    To produce a code block in Markdown, simply indent every line of the block by at least 4 spaces or 1 tab. 
    
##6. LINKS&IMAGES
    [This is a link](http://xxx.xxx.com)

or

    [This is a link] []
    and give definition later
    [This is a link]:http://xx.xx.com
    
The later format is more readable in raw.

And for image is similar:

    ![image](httt://url.to.resource)
    
And another short form for url link
    
    <http://xxx.xxx.com>
    
##7. EMPHASIS
    *xxx*:      emphasis
    **xxx**:    strong



