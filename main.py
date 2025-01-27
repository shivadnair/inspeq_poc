import bedrock_integ
import inspeq_eval

if __name__ == "__main__":

    #Prompt from the user
    prompt = "What is the capital of India"
    
    #Pre-evaluating the user prompt
    response = inspeq_eval.inspeq_metric_eval(prompt)

    if response:
        print("Pre-evaluation of the user prompt successful:")
        print(response)
    else:
        print("Error during pre-evaluation")

    #Initializing the Bedrock client
    bedrock_client = bedrock_integ.initialize_bedrock_client()

    if bedrock_client:
        #Generating the response
        bedrock_response = bedrock_integ.generate_resp(bedrock_client, prompt)
        
        if response:
            print("Generated response:")
            print(bedrock_response)
        else:
            print("Error generating response")

    #Evaluate the response
    metric_list = ["ANSWER_RELEVANCE", "FACTUAL_CONSISTENCY", "RESPONSE_TONE"]

    inspeq_eval_response = inspeq_eval.inspeq_metric_eval(prompt, bedrock_response, metric_list)

    if inspeq_eval_response:
        print("Post-evaluation of the AI response successful:")
        print(inspeq_eval_response)
    else:
        print("Error during post-evaluation")