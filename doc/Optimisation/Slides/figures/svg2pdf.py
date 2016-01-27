import os

svgdir = "svg/"
pdfdir = ""

pattern = "inkscape -f {1}{0}.svg -A {2}{0}.pdf --export-latex -D"
files = os.listdir("./" + svgdir)
for f in files:
  if os.path.isfile(svgdir + f):
    words = f.split('.')
    if words[-1] == "svg":
      root = f[:-4]
      os.system(pattern.format(root, svgdir, pdfdir))
    
