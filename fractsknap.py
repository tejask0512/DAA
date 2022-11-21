class Item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight

def fract_knap(W,arr):
    arr.sort(key=lambda x: (x.value/x.weight),  reverse=True)
    final_value=0.0

    for item in arr:
        if item.weight<=W:
            W=W-item.weight
            final_value+=item.value
        else:
            final_value=(item.value*W)/(item.weight)
    return final_value

W=50
arr=[Item(100,20),Item(150,50),Item(200,80)]

max_prof=fract_knap(W,arr)
print(max_prof)
