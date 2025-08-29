# API Key Configuration Implementation Plan

## Steps to Implement User-Provided API Keys

### 1. Frontend UI Changes
- [x] Add config button/section in index.html
- [x] Create modal/dialog for API key input
- [x] Add styling for config section in style.css
- [x] Implement localStorage for saving API keys

### 2. Frontend JavaScript Changes
- [x] Add event listeners for config button
- [x] Implement API key loading/saving from localStorage
- [x] Modify fetch requests to include user API keys
- [ ] Add validation for API keys

### 3. Backend Changes
- [x] Modify /llm/query endpoint to accept API keys from request
- [x] Update function calls to use user-provided keys or fallback to env
- [ ] Add error handling for invalid API keys

### 4. Testing
- [ ] Test UI functionality
- [ ] Test API key saving/loading
- [ ] Test backend with user-provided keys
- [ ] Test fallback to environment variables

## API Services to Configure
- AssemblyAI (Speech-to-Text)
- Murf AI (Text-to-Speech) 
- Gemini (LLM)
- WeatherAPI (Weather service)
