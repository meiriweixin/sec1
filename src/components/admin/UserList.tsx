import { useState } from 'react';
import { SglearnUser } from '@/lib/supabase';
import { deleteUser, toggleUserStatus } from '@/lib/user-management';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Switch } from '@/components/ui/switch';
import { toast } from 'sonner';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from '@/components/ui/alert-dialog';
import { Trash2 } from 'lucide-react';

interface UserListProps {
  users: SglearnUser[];
  onUserDeleted: () => void;
  onUserUpdated: () => void;
}

export function UserList({ users, onUserDeleted, onUserUpdated }: UserListProps) {
  const [deleteUserId, setDeleteUserId] = useState<string | null>(null);
  const [deletingId, setDeletingId] = useState<string | null>(null);
  const [togglingId, setTogglingId] = useState<string | null>(null);

  const handleDelete = async () => {
    if (!deleteUserId) return;

    setDeletingId(deleteUserId);
    try {
      const success = await deleteUser(deleteUserId);
      if (success) {
        toast.success('User deleted successfully');
        onUserDeleted();
      } else {
        toast.error('Failed to delete user');
      }
    } catch (error: any) {
      toast.error(error.message || 'Failed to delete user');
    } finally {
      setDeletingId(null);
      setDeleteUserId(null);
    }
  };

  const handleToggleStatus = async (userId: string, currentStatus: boolean) => {
    setTogglingId(userId);
    try {
      const success = await toggleUserStatus(userId, !currentStatus);
      if (success) {
        toast.success(`User ${!currentStatus ? 'activated' : 'deactivated'} successfully`);
        onUserUpdated();
      } else {
        toast.error('Failed to update user status');
      }
    } catch (error) {
      toast.error('Failed to update user status');
    } finally {
      setTogglingId(null);
    }
  };

  const formatDate = (dateString: string | null | undefined) => {
    if (!dateString) return 'Never';
    return new Date(dateString).toLocaleString();
  };

  return (
    <>
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Email</TableHead>
              <TableHead>Name</TableHead>
              <TableHead>Role</TableHead>
              <TableHead>Status</TableHead>
              <TableHead>Last Login</TableHead>
              <TableHead>Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {users.length === 0 ? (
              <TableRow>
                <TableCell colSpan={6} className="text-center text-muted-foreground">
                  No users found
                </TableCell>
              </TableRow>
            ) : (
              users.map((user) => (
                <TableRow key={user.id}>
                  <TableCell className="font-medium">{user.email}</TableCell>
                  <TableCell>{user.name}</TableCell>
                  <TableCell>
                    {user.is_admin ? (
                      <Badge variant="default">Admin</Badge>
                    ) : (
                      <Badge variant="secondary">User</Badge>
                    )}
                  </TableCell>
                  <TableCell>
                    <div className="flex items-center gap-2">
                      <Switch
                        checked={user.is_active}
                        onCheckedChange={() => handleToggleStatus(user.id, user.is_active)}
                        disabled={togglingId === user.id}
                      />
                      <span className="text-sm">
                        {user.is_active ? 'Active' : 'Inactive'}
                      </span>
                    </div>
                  </TableCell>
                  <TableCell className="text-sm text-muted-foreground">
                    {formatDate(user.last_login_at)}
                  </TableCell>
                  <TableCell>
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => setDeleteUserId(user.id)}
                      disabled={deletingId === user.id}
                    >
                      <Trash2 className="h-4 w-4" />
                    </Button>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </div>

      <AlertDialog open={!!deleteUserId} onOpenChange={(open) => !open && setDeleteUserId(null)}>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Are you sure?</AlertDialogTitle>
            <AlertDialogDescription>
              This will permanently delete this user. This action cannot be undone.
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>Cancel</AlertDialogCancel>
            <AlertDialogAction onClick={handleDelete}>Delete</AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </>
  );
}
