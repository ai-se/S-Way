### More generations implies better results?  
Reference: https://github.com/ai-se/storm/issues/20  
GALE0 vs GALE  
GALE0: Number of members in the population is 10X = 1000  
GALE: Number of members in the population = 100 (Number of generations=20)  

GALE_NO_MUTATION: Gale but no mutation -> GALE who randomly generates solution every generation -> Shown in green.  

![figure01_dtlz1_9_5_](https://cloud.githubusercontent.com/assets/6147456/11126899/4409e2c0-893f-11e5-958d-5de790b71ffe.png)
![figure02_dtlz2_14_5_](https://cloud.githubusercontent.com/assets/6147456/11126896/44086cce-893f-11e5-975d-b021a3da0c02.png)
![figure03_dtlz3_14_5_](https://cloud.githubusercontent.com/assets/6147456/11126900/440a2d2a-893f-11e5-9f85-ab6e730b9574.png)
![figure04_dtlz4_14_5_](https://cloud.githubusercontent.com/assets/6147456/11126895/4404b886-893f-11e5-9c8d-3af6a516c450.png)
![figure05_dtlz1_7_3_](https://cloud.githubusercontent.com/assets/6147456/11126898/44099a4a-893f-11e5-9b52-b8687fb95c0d.png)
![figure06_dtlz2_12_3_](https://cloud.githubusercontent.com/assets/6147456/11126897/440903f0-893f-11e5-8e03-888212c5e4b7.png)
![figure07_dtlz3_12_3_](https://cloud.githubusercontent.com/assets/6147456/11126901/440fa246-893f-11e5-9d63-745d2e4f31f2.png)
![figure08_dtlz4_12_3_](https://cloud.githubusercontent.com/assets/6147456/11126902/4417569e-893f-11e5-9a6f-84b7577e2914.png)
![figure09_dtlz1_12_8_](https://cloud.githubusercontent.com/assets/6147456/11126905/4419154c-893f-11e5-86db-96707e6ff4e6.png)
![figure10_dtlz2_17_8_](https://cloud.githubusercontent.com/assets/6147456/11126904/4417bcb0-893f-11e5-8bc1-159c779b2e1c.png)
![figure11_dtlz3_17_8_](https://cloud.githubusercontent.com/assets/6147456/11126903/44177ed0-893f-11e5-9e65-f11e5a3db1f8.png)
![figure12_dtlz4_17_8_](https://cloud.githubusercontent.com/assets/6147456/11126906/4418f972-893f-11e5-96da-941f71fd4c71.png)
![figure21_web_portal_](https://cloud.githubusercontent.com/assets/6147456/11126907/441c05e0-893f-11e5-8c8c-3b4fa481afbd.png)

Conclusion. GALE0 and GALE are similiar. I.e. more generations does not implies better results

### Mutation works?
Reference: https://github.com/ai-se/storm/issues/21
```
{'Repeats': 5, 'Population_Size': 100, 'No_of_Generations': 20} {'EPSILON': 1.0, 'DELTA': 1, 'GAMMA': 0.15, 'LAMBDA': 3}
```
![screenshot 2015-11-11 16 47 54](https://cloud.githubusercontent.com/assets/6147456/11103984/119fe66e-8894-11e5-8758-34092daa2b4a.png)


```
{'Repeats': 5, 'Population_Size': 100, 'No_of_Generations': 20} {'EPSILON': 1.0, 'DELTA': 3, 'GAMMA': 0.15, 'LAMBDA': 3}
```
![screenshot 2015-11-11 16 48 32](https://cloud.githubusercontent.com/assets/6147456/11103988/16a550c2-8894-11e5-9d8c-d64a7d9e17ad.png)

Conclusion: the mutation works. But the value of delta matters.
TODO: 1. confirm this conclusion; 2. how to determine the delta; 3. does the shape of frontier matters?

