import requests
import time
import sys

def run_integration_test():
    base_url = "http://localhost:8080"
    print(f"Submitting query to {base_url}/main...")
    
    response = requests.post(f"{base_url}/main", json={"ticker": "MSFT"})
    
    if response.status_code != 202:
        print(f"Error submitting request: HTTP {response.status_code}")
        print(response.text)
        sys.exit(1)
        
    data = response.json()
    req_id = data.get("request_id")
    print(f"Got Request ID: {req_id}")
    
    max_wait = 30
    elapsed = 0
    
    while elapsed < max_wait:
        status_res = requests.get(f"{base_url}/status/{req_id}").json()
        status = status_res.get("status")
        
        if status == "done":
            result = status_res.get("result", {})
            print(f"\nWorkflow Completed! Result: {result}")
            
            # Validation assertions
            assert "MSFT" in result.get("company_name", ""), "Missing expected company name."
            assert "This is an LLM generated response to" in result.get("competitors", ""), "VllmAgent response formatting missing."
            assert result.get("stock_price") == 100.0, "FinanceAgent did not return 100.0"
            
            print("\nIntegration test passed. All validations successful.")
            sys.exit(0)
            
        if status == "error":
            print(f"Workflow hit an error: {status_res.get('error')}")
            sys.exit(1)
            
        print(f"Status: {status} ... waiting")
        time.sleep(1)
        elapsed += 1
        
    print(f"Timed out after {max_wait}s waiting for workflow completion.")
    sys.exit(1)

if __name__ == "__main__":
    run_integration_test()
