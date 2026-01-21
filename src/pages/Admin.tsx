import { useState, useEffect } from 'react';
import { fetchAllUsers } from '@/lib/user-management';
import { SglearnUser } from '@/lib/supabase';
import { UserList } from '@/components/admin/UserList';
import { AddUserDialog } from '@/components/admin/AddUserDialog';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Search, Users } from 'lucide-react';

export default function Admin() {
  const [users, setUsers] = useState<SglearnUser[]>([]);
  const [filteredUsers, setFilteredUsers] = useState<SglearnUser[]>([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(true);

  const loadUsers = async () => {
    setLoading(true);
    const data = await fetchAllUsers();
    if (data) {
      setUsers(data);
      setFilteredUsers(data);
    }
    setLoading(false);
  };

  useEffect(() => {
    loadUsers();
  }, []);

  useEffect(() => {
    if (searchQuery.trim() === '') {
      setFilteredUsers(users);
    } else {
      const query = searchQuery.toLowerCase();
      const filtered = users.filter(
        (user) =>
          user.email.toLowerCase().includes(query) ||
          user.name.toLowerCase().includes(query)
      );
      setFilteredUsers(filtered);
    }
  }, [searchQuery, users]);

  return (
    <div className="container mx-auto py-8 px-4">
      <div className="flex flex-col gap-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold">User Management</h1>
            <p className="text-muted-foreground mt-2">
              Manage user access and permissions
            </p>
          </div>
          <AddUserDialog onUserAdded={loadUsers} />
        </div>

        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Users className="h-5 w-5" />
              All Users ({filteredUsers.length})
            </CardTitle>
            <CardDescription>
              View and manage all registered users
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="relative">
              <Search className="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground" />
              <Input
                placeholder="Search by email or name..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="pl-8"
              />
            </div>

            {loading ? (
              <div className="text-center py-8 text-muted-foreground">
                Loading users...
              </div>
            ) : (
              <UserList
                users={filteredUsers}
                onUserDeleted={loadUsers}
                onUserUpdated={loadUsers}
              />
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
