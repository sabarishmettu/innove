Here is an example of a complete Python program that allows a user to upload a photo, crop it, and save the cropped image.

This program uses Flask, a Python web framework, to handle HTTP requests and responses. It defines two routes: the root route, which displays an HTML form for uploading a photo and selecting a crop region, and the /crop route, which receives the form data, crops the uploaded photo, and displays the cropped image.

The program uses the PIL library to manipulate images. It saves the uploaded photo to disk, opens it using PIL, crops it using the provided parameters, and saves the cropped image to disk.

To use this program, you would need to create two HTML templates: index.html, which displays the upload form, and crop.html, which displays the cropped image. Here is an example of index.html