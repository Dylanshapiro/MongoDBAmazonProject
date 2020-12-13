python3 ProductUnitTest.py | grep -v "initandlisten" | grep -v "ERROR:"  > product.results; cat product.results | grep error;
python3 CustomerUnitTest.py | grep -v "initandlisten" | grep -v "ERROR:" > customer.results; cat customer.results | grep error;
python3 OrderDocumentUnitTest.py | grep -v "initandlisten" | grep -v "ERROR:" > orderdoc.results; cat orderdoc.results | grep error;