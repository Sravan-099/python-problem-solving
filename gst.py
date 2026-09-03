service_fee = float(input("Enter service fee: "))
gst = service_fee * 18 / 100
final_amount = service_fee + gst

print("GST:", gst)
print("Final amount:", final_amount)