import { useRouter } from 'next/router';
import axios from 'axios';
import { useState } from 'react';

const TournamentRegister = () => {
  const router = useRouter();
  const { id } = router.query;
  const [playerId, setPlayerId] = useState('');
  const [message, setMessage] = useState('');

  const handleRegister = async () => {
    try {
      const response = await axios.post(`/api/v1/tournaments/${id}/register`, { player_id: playerId });
      setMessage(response.data.registration_status);
    } catch (error) {
      setMessage('Failed to register for the tournament');
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Register for Tournament</h1>
      <input
        type="text"
        value={playerId}
        onChange={(e) => setPlayerId(e.target.value)}
        placeholder="Enter Player ID"
        className="border p-2 mb-4 w-full"
      />
      <button onClick={handleRegister} className="bg-blue-500 text-white p-2 rounded">
        Register
      </button>
      {message && <p className="mt-4">{message}</p>}
    </div>
  );
};

export default TournamentRegister;