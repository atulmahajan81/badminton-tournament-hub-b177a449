import Link from 'next/link';

const TournamentCard = ({ tournament }: { tournament: any }) => {
  return (
    <div className="bg-white shadow-md rounded p-4">
      <h2 className="font-bold text-xl mb-2">{tournament.name}</h2>
      <p className="mb-2">Location: {tournament.location}</p>
      <p className="mb-2">Date: {new Date(tournament.date).toLocaleDateString()}</p>
      <Link href={`/tournaments/${tournament.id}`}>
        <a className="text-blue-500">View Details</a>
      </Link>
    </div>
  );
};

export default TournamentCard;