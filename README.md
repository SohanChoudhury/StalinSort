# Stalin Sort
The totally legit O(n) sorting algorithm. Guaranteed to work every time. In every case. No amortized cost preprocessing bulls***.

## In-depth technical explanation very technical
Stalin sort is a single pass O(n) sorting algorithm. So you iterate through the list of elements, checking that each element is in the desired ordering (the implementation in this order sorts in an increasing order). Any element which is out of order is eliminated. In the end this gives us a sorted list.
