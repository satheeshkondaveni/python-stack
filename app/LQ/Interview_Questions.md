1. 1. How you can resolve the Memory Exhaustion (Limited memory issue) in Python FastAPI applications?
2. Causes:-
3. Large request/response - pydantic/pandas payload(JSON, images, files).
3. Memory Leaks (Objects not released)
4. Blocking huge I/O operation or running multiple backend thread.
5. in-memory storage/ caching
6. ANS:- 
7. Load the data paginations with date or some other filters for DBs or Incremental approaches.
7. Caching for temporary data storage, use like Redis caching.
8. Celeray queues and run the thread in background in parallel mode, create celery task and stream the large files or process files in chuncks.
9. Use the GC collectors to clean the unused objects.

2. If we have millions of large files in S3 bucket, How you can load the files into your Python FastAPI Application?
3. Cause:-
4. Two problems: 
4. 1. direct file searching is not possible in S3, it will crash the API and S3 service calls.
5.   Ans: Create the metadata indexes in Metadata tables in the DB (PostgreSQL/DynamoDB)
6.    columns: id, filename,file_size, file_content_type, create_date, content type, s3 path, index_for_vectory,chunk_ids_for_vector,  
       Then Fast Serach, Filtering, Pagination+Cursor-Based Fetch, AI-Based Search (vector) will become easy.
      workflow: User Request --> DB Query --> Get S3 path -> Fecth only required files.
6. 2.Large file loading into the application running memory is the problem(Never do this practice)
7. Chucking the file and load from the S3, if those are .csv then use the S3 Select Queries and get required data onlhy instead of loading entire file.
8. Backend use OCta-streamer response APIs and UI will load steam based.
9. Use the Redis catches and Celery Queues.

3. How did you handiled the documents for the AWS Bedrock LLM, the documents uploaded by the user form the UI chatbot?



9. 
6. 
