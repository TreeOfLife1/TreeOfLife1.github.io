#Make a folder
#Put this program in that folder
#Run this program

htmlFile = open("index.html", "w")
cssFile = open("styles.css", "w")

htmlContent = '''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="styles.css">
        <title>Page title</title>
    </head>
    <body>
        <div class="Content">
      
        </div>
    </body>
</html>'''

cssContent = '''body {
  background-color: lightgray;
  margin: 0;
}
.Content {
  width: 100vw;
  height: 100vmax;
  max-width: 1090px;
  margin: 0 auto;
  background-color: white;
}
'''


print(htmlContent, file=htmlFile)
print(cssContent, file=cssFile)

htmlFile.close()
cssFile.close()
