import { useState } from 'react';
import { CheckCircle, Edit, Save, X, BookOpen, FileQuestion } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Badge } from '@/components/ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import type { GeneratedContent } from '@/lib/azure-openai';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

interface ContentReviewProps {
  content: GeneratedContent;
  onSave: (content: GeneratedContent) => void;
  onCancel: () => void;
}

export function ContentReview({ content: initialContent, onSave, onCancel }: ContentReviewProps) {
  const [content, setContent] = useState<GeneratedContent>(initialContent);
  const [editingSection, setEditingSection] = useState<string | null>(null);
  const [editingExercise, setEditingExercise] = useState<string | null>(null);

  const updateTitle = (field: 'title' | 'title_zh', value: string) => {
    setContent({ ...content, [field]: value });
  };

  const updateDescription = (field: 'description' | 'description_zh', value: string) => {
    setContent({ ...content, [field]: value });
  };

  const updateSection = (sectionId: string, field: string, value: string) => {
    setContent({
      ...content,
      sections: content.sections.map((section) =>
        section.id === sectionId ? { ...section, [field]: value } : section
      ),
    });
  };

  const updateExercise = (exerciseId: string, field: string, value: any) => {
    setContent({
      ...content,
      exercises: content.exercises.map((exercise) =>
        exercise.id === exerciseId ? { ...exercise, [field]: value } : exercise
      ),
    });
  };

  const deleteSection = (sectionId: string) => {
    if (confirm('Delete this section?')) {
      setContent({
        ...content,
        sections: content.sections.filter((s) => s.id !== sectionId),
      });
    }
  };

  const deleteExercise = (exerciseId: string) => {
    if (confirm('Delete this exercise?')) {
      setContent({
        ...content,
        exercises: content.exercises.filter((e) => e.id !== exerciseId),
      });
    }
  };

  const handleSave = () => {
    // Validate content before saving
    if (!content.title || !content.description) {
      alert('Please fill in title and description');
      return;
    }

    if (content.sections.length === 0) {
      alert('Chapter must have at least one section');
      return;
    }

    if (content.exercises.length === 0) {
      alert('Chapter must have at least one exercise');
      return;
    }

    onSave(content);
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50 overflow-y-auto">
      <Card className="w-full max-w-5xl p-6 bg-white dark:bg-gray-800 my-8">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-2xl font-bold">Review Generated Content</h2>
            <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
              Review and edit before saving as new chapter
            </p>
          </div>
          <Button variant="ghost" size="sm" onClick={onCancel}>
            <X className="w-4 h-4" />
          </Button>
        </div>

        {/* Chapter Metadata */}
        <div className="space-y-4 mb-6">
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="text-sm font-medium">Title (English)</label>
              <Input
                value={content.title}
                onChange={(e) => updateTitle('title', e.target.value)}
                className="mt-1"
              />
            </div>
            <div>
              <label className="text-sm font-medium">Title (Chinese)</label>
              <Input
                value={content.title_zh}
                onChange={(e) => updateTitle('title_zh', e.target.value)}
                className="mt-1"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="text-sm font-medium">Description (English)</label>
              <Textarea
                value={content.description}
                onChange={(e) => updateDescription('description', e.target.value)}
                className="mt-1"
                rows={2}
              />
            </div>
            <div>
              <label className="text-sm font-medium">Description (Chinese)</label>
              <Textarea
                value={content.description_zh}
                onChange={(e) => updateDescription('description_zh', e.target.value)}
                className="mt-1"
                rows={2}
              />
            </div>
          </div>

          <div className="flex gap-2">
            <Badge variant="secondary">{content.sections.length} Sections</Badge>
            <Badge variant="secondary">{content.exercises.length} Exercises</Badge>
            <Badge variant="secondary">Grade: {content.gradeLevel.toUpperCase()}</Badge>
          </div>
        </div>

        <Tabs defaultValue="sections" className="w-full">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="sections">
              <BookOpen className="w-4 h-4 mr-2" />
              Lesson Sections ({content.sections.length})
            </TabsTrigger>
            <TabsTrigger value="exercises">
              <FileQuestion className="w-4 h-4 mr-2" />
              Exercises ({content.exercises.length})
            </TabsTrigger>
            <TabsTrigger value="objectives">
              <CheckCircle className="w-4 h-4 mr-2" />
              Objectives
            </TabsTrigger>
          </TabsList>

          <TabsContent value="sections" className="space-y-4 max-h-[500px] overflow-y-auto pr-2">
            {content.sections.map((section, index) => (
              <Card key={section.id} className="p-4">
                <div className="flex items-center justify-between mb-3">
                  <h3 className="font-semibold">Section {index + 1}</h3>
                  <div className="flex gap-2">
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() =>
                        setEditingSection(editingSection === section.id ? null : section.id)
                      }
                    >
                      <Edit className="w-4 h-4" />
                    </Button>
                    <Button variant="ghost" size="sm" onClick={() => deleteSection(section.id)}>
                      <X className="w-4 h-4 text-red-600" />
                    </Button>
                  </div>
                </div>

                {editingSection === section.id ? (
                  <div className="space-y-3">
                    <Input
                      value={section.title}
                      onChange={(e) => updateSection(section.id, 'title', e.target.value)}
                      placeholder="Title (English)"
                    />
                    <Input
                      value={section.title_zh}
                      onChange={(e) => updateSection(section.id, 'title_zh', e.target.value)}
                      placeholder="Title (Chinese)"
                    />
                    <Textarea
                      value={section.content}
                      onChange={(e) => updateSection(section.id, 'content', e.target.value)}
                      placeholder="Content (English, markdown formatted)"
                      rows={8}
                      className="font-mono text-sm"
                    />
                    <Textarea
                      value={section.content_zh}
                      onChange={(e) => updateSection(section.id, 'content_zh', e.target.value)}
                      placeholder="Content (Chinese)"
                      rows={8}
                      className="font-mono text-sm"
                    />
                  </div>
                ) : (
                  <div>
                    <h4 className="font-medium mb-2">{section.title}</h4>
                    <div className="prose dark:prose-invert prose-sm max-w-none">
                      {(() => {
                        const content = section.content;
                        const safeContent = Array.isArray(content)
                          ? content.join('\n\n')
                          : typeof content === 'string'
                            ? content
                            : String(content || '');

                        const displayContent = safeContent.slice(0, 300) + (safeContent.length > 300 ? '...' : '');
                        return (
                          <ReactMarkdown
                            remarkPlugins={[remarkGfm, remarkMath]}
                            rehypePlugins={[rehypeKatex]}
                          >
                            {displayContent}
                          </ReactMarkdown>
                        );
                      })()}
                    </div>
                  </div>
                )}
              </Card>
            ))}
          </TabsContent>

          <TabsContent value="exercises" className="space-y-4 max-h-[500px] overflow-y-auto pr-2">
            {content.exercises.map((exercise, index) => (
              <Card key={exercise.id} className="p-4">
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center gap-2">
                    <h3 className="font-semibold">Exercise {index + 1}</h3>
                    <Badge>{exercise.type}</Badge>
                    <Badge variant={exercise.difficulty === 'hard' ? 'destructive' : 'secondary'}>
                      {exercise.difficulty}
                    </Badge>
                  </div>
                  <div className="flex gap-2">
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() =>
                        setEditingExercise(editingExercise === exercise.id ? null : exercise.id)
                      }
                    >
                      <Edit className="w-4 h-4" />
                    </Button>
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => deleteExercise(exercise.id)}
                    >
                      <X className="w-4 h-4 text-red-600" />
                    </Button>
                  </div>
                </div>

                {editingExercise === exercise.id ? (
                  <div className="space-y-3">
                    <Textarea
                      value={exercise.prompt}
                      onChange={(e) => updateExercise(exercise.id, 'prompt', e.target.value)}
                      placeholder="Question (English)"
                      rows={3}
                    />
                    {exercise.choices && (
                      <div className="space-y-2">
                        {exercise.choices.map((choice, i) => (
                          <Input
                            key={i}
                            value={choice}
                            onChange={(e) => {
                              const newChoices = [...exercise.choices!];
                              newChoices[i] = e.target.value;
                              updateExercise(exercise.id, 'choices', newChoices);
                            }}
                            placeholder={`Choice ${i + 1}`}
                          />
                        ))}
                      </div>
                    )}
                    <Input
                      type="number"
                      value={typeof exercise.answer === 'number' ? exercise.answer : 0}
                      onChange={(e) =>
                        updateExercise(exercise.id, 'answer', parseInt(e.target.value))
                      }
                      placeholder="Correct answer index (0-based)"
                    />
                  </div>
                ) : (
                  <div>
                    <div className="mb-2 prose dark:prose-invert prose-sm max-w-none">
                      <ReactMarkdown
                        remarkPlugins={[remarkGfm, remarkMath]}
                        rehypePlugins={[rehypeKatex]}
                      >
                        {exercise.prompt}
                      </ReactMarkdown>
                    </div>
                    {exercise.choices && (
                      <ul className="text-sm space-y-1 ml-4">
                        {exercise.choices.map((choice, i) => (
                          <li
                            key={i}
                            className={
                              exercise.answer === i ? 'text-green-600 font-semibold' : ''
                            }
                          >
                            {i + 1}. {choice}
                            {exercise.answer === i && ' ✓'}
                          </li>
                        ))}
                      </ul>
                    )}
                  </div>
                )}
              </Card>
            ))}
          </TabsContent>

          <TabsContent value="objectives" className="space-y-3">
            <div>
              <h3 className="font-semibold mb-2">Learning Objectives (English)</h3>
              <ul className="space-y-2">
                {content.objectives.map((obj, i) => (
                  <li key={i} className="flex items-start gap-2">
                    <CheckCircle className="w-4 h-4 mt-1 text-green-600 flex-shrink-0" />
                    <span>{obj}</span>
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-2">Learning Objectives (Chinese)</h3>
              <ul className="space-y-2">
                {content.objectives_zh.map((obj, i) => (
                  <li key={i} className="flex items-start gap-2">
                    <CheckCircle className="w-4 h-4 mt-1 text-green-600 flex-shrink-0" />
                    <span>{obj}</span>
                  </li>
                ))}
              </ul>
            </div>
          </TabsContent>
        </Tabs>

        <div className="flex justify-end gap-3 mt-6 pt-6 border-t">
          <Button variant="outline" onClick={onCancel}>
            Cancel
          </Button>
          <Button onClick={handleSave} className="bg-green-600 hover:bg-green-700">
            <Save className="w-4 h-4 mr-2" />
            Save Chapter
          </Button>
        </div>
      </Card>
    </div>
  );
}
