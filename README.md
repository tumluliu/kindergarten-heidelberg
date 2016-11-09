# Kindergarten information of Heidelberg

Not all kindergartens in Heidelberg can be found from online map services like Google Maps. There is a [kindergarten list document](http://www.zuv.uni-heidelberg.de/md/zuv/international/gaeste/childcare_0-6_sept2014_docx.pdf) with detailed contact info of 2014 provided by Universitaet Heidelberg. Unfortunately, the document is in PDF format. So it is too troublesome to locate the kindergartens on a map, which makes me difficult to make a decision on kindergarten application. 

Therefore, I decided doing some transformation work to make the kindergarten
info list map-friendly. The Basic steps are:

1. Extract text from the PDF file
2. Reorganize the kindergarten info items into CSV format
3. Extract the address for each kindergarten
4. Find the longitude and latitude location via geocoding service
5. Append the geospatial info back to the CSV
6. Upload the CSV to CartoDB and visualize it
