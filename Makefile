FC=f95
TARGET=Kendall-new

all: $(TARGET)

$(TARGET): $(TARGET).for
	$(FC) -o $(TARGET) $(TARGET).for

clean:
	rm -f $(TARGET) 
	
check: all
	python3 kendalWrapper.py
