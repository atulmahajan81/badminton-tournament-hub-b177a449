import apiClient from '@/lib/api';

export const fetchTournaments = async () => {
  const response = await apiClient.get('/api/v1/tournaments');
  return response.data;
};

export const fetchTournamentById = async (id: string) => {
  const response = await apiClient.get(`/api/v1/tournaments/${id}`);
  return response.data;
};