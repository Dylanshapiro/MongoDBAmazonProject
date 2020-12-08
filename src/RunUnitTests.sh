python3 ProductUnitTest.py | grep -v "initandlisten" > product.results; cat product.results | grep error;
python3 CustomerUnitTest.py | grep -v "initandlisten" > customer.results; cat customer.results | grep error;
python3 OrderDocumentUnitTest.py | grep -v "initandlisten" > orderdoc.results; cat orderdoc.results | grep error;