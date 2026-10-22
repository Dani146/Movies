const API_URL = "http://localhost:8000";

export async function getWelcomeMessage(): Promise<string> {
  const response = await fetch(`${API_URL}/welcome`);

  if (!response.ok) {
    throw new Error(`HTTP error: ${response.status}`);
  }

  const data: { message: string } = await response.json();

  return data.message;
}