import { useAuthStore } from "../store/authStore";

export function testAuthStore() {
  console.log("Running authStore unit assertions...");
  
  const state = useAuthStore.getState();
  
  // Assert initial state is unauthenticated
  if (state.isAuthenticated !== false) {
    throw new Error("Assert failed: initial isAuthenticated must be false");
  }
  
  // Mock login event
  state.login("mock_access", "mock_refresh", "TRADER", {
    username: "test_trader",
    email: "test@alphaforge.ai"
  });
  
  const loggedInState = useAuthStore.getState();
  if (loggedInState.isAuthenticated !== true || loggedInState.role !== "TRADER") {
    throw new Error("Assert failed: login authentication mapping error");
  }
  
  // Mock logout event
  loggedInState.logout();
  const loggedOutState = useAuthStore.getState();
  if (loggedOutState.isAuthenticated !== false || loggedOutState.accessToken !== null) {
    throw new Error("Assert failed: logout clear error");
  }
  
  console.log("All authStore unit assertions passed successfully.");
}
