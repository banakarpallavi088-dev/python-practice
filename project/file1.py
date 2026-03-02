class InventoryItem:
    def __init__(self,name,id,quntity,price):
        self.name=name
        self.id=id
        self.quntity=quntity
        self.price=price
    
def View_allproduct():
    print()

print("inventory Manegement system ")
yes=1
while yes!=0:
    print("1. Add Product\n2. View All Products\n3. Search Product (Using ID)\n4. Update Product\n5. Delete Product\n6. Purchase Product (Reduce Quantity)\n7. Low Stock Alert\n")
    ch=int(input("Enter your choice"))
    match ch:
        case 1:Add_product()
        case 2:View_allproduct()
        case 3:search_product()
        case 4:update_product()
        case 5:delete_product()
        case 6:purchase_product()
        case _:
            print("invalid choice")

    yes=int(input("do you went to continue 1/0"))






