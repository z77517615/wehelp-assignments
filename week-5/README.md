要求三:<br/>
● 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。<br/>
● 使用 SELECT 指令取得所有在 member 資料表中的會員資料。<br/>


![image](https://user-images.githubusercontent.com/94062367/150899881-b05d1ef5-1955-4f35-97fd-2dd9ff79184c.png)
![image](https://user-images.githubusercontent.com/94062367/150899931-0c962859-1e6c-430b-a76b-3421701e21d2.png)


● 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。<br/>
● 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )<br/>
![image](https://user-images.githubusercontent.com/94062367/150900267-199d5f95-35e7-48be-9b44-676ff8af81e8.png)

● 使用 SELECT 指令取得欄位 username 是 test 的會員資料。<br/>
在此新增id = 6 , Rob uersname = test , password = key<br/>
![image](https://user-images.githubusercontent.com/94062367/150900649-4ee114b6-ae4a-45d3-ae3b-2a48206d55bd.png)
![image](https://user-images.githubusercontent.com/94062367/150900675-fa355cfa-917b-4ce5-8c6d-9dd5a316256a.png)

● 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2<br/>
![image](https://user-images.githubusercontent.com/94062367/150901085-e5f68cfd-ff4a-47b9-93ad-c6799ce03c73.png)
<br/>
<br/>
<br/>
要求四：SQL Aggregate Functions<br/>
● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。<br/>
![image](https://user-images.githubusercontent.com/94062367/150902163-7f386291-6bd2-4da1-9ca0-6d2745f2c5ed.png)
<br/>
<br/>
更新follower_count 資訊<br/>
![image](https://user-images.githubusercontent.com/94062367/150903216-b2d110a8-df6c-457d-aefd-9868e99238f2.png)
<br/>
● 取得 member 資料表中，所有會員 follower_count 欄位的總和。<br/>
● 取得 member 資料表中，所有會員 follower_count 欄位的平均數<br/>
![image](https://user-images.githubusercontent.com/94062367/150903537-d235a372-aee2-4602-ba69-3e82fb085c0e.png)
<br/>
<br/>
要求五：SQL JOIN (Optional)<br/>
1. 在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定：<br/>
![image](https://user-images.githubusercontent.com/94062367/150906499-44150ce3-a806-49d5-8ac9-d0cdc84704f0.png)



