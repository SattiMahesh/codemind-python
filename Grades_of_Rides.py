hf,sp,sf=map(int,input().split())
if hf>50 and sp>60 and sf>100:
    print("10")
elif hf>50 and sp>60:
    print("9")
elif sp>60 and sf>100:
    print("8")
elif sf>100 and hf>50:
    print("7")
elif sf>100 or sp>60 or hf>50:
    print("6")
else:
    print("5")
