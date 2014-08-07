Welcome to the Court Seal Rookery
=================================

This is a collection of court seals that can be cloned and used in any project. 
Original files can be found in the `orig` directory and converted versions can 
be found in the numerical directories. 

The goal of this project is to collect and maintain an updated repository of all
the seals that courts have created and to create seals for those rare courts 
that lack them altogether.


Contributing
------------

This project is blissfully easy to contribute to and we need lots of help 
gathering or making files. The process for this is pretty simple. 
 
 1. Find or make the image and ensure it follows our quality guidelines 
 (below).
 1. Add the image file to the `orig` directory.
 1. Regenerate the converted versions by running `convert_images.py` (note that
 this requires imagemagick).
 1. Edit `seals.json` to include the relevant fields for your new file.
  
That's it!


Quality Guidelines
------------------

Fact is, images are hard to work with and courts don't always do the best job.
Follow these guidelines so we can have nice things:

1. Convert your original file to `png` or `svg`, as appropriate. If you have the
`ps` file, include that as well.
1. If you use transparency or the file has it, make sure the file looks OK on 
a background other than white. If it looks bizarre on an orange or blue 
background, fix it by adding a white layer on the bottom.
1. Trim any extraneous margins and if the seal is circular, make the corners 
transparent.
1. If the item was previously a `jpeg`, it's good to clean up the splotchiness 
created by the `jpeg` compression. You'll see it if you zoom in.  


Copyright
---------

Two things. First, if you are creating original work, please consider signing
and emailing a contributor license to us so that we may protect the work later, 
if needed. We do this because we have a lot of experience with IP litigation,
and this is a good way to protect a project.

Second, if you're just curious about the copyright of this repository, see the 
License file for details. The short version of this is you can pretty much use 
it however you desire.
