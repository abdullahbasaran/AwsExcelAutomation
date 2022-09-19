import os
import json
import pandas as pd

#json string in file format
command = "aws ec2 describe-instances --query \"Reservations[*].Instances[].{ instance_id: InstanceId, type: InstanceType, stats: State.Name, disks: BlockDeviceMappings[*].Ebs.VolumeId, p_ip: NetworkInterfaces[*].PrivateIpAddresses[].PrivateIpAddress, name: Tags[?Key == `Name`].Value, cpu: CpuOptions.CoreCount, platform: PlatformDetails}\" > out22.json"
os.system(command) 


# read json to data frame                                                                                                    
df = pd.read_json("out22.json")
print(df)
df.to_excel("data.xlsx")