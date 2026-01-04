import { auth } from "@clerk/nextjs/server"
import { redirect } from "next/navigation"
import Link from "next/link"
import { FileText, Search, BookOpen, FolderOpen, PlayCircle } from "lucide-react"

export default async function DashboardPage() {
  const { userId } = await auth()

  if (!userId) {
    redirect("/sign-in")
  }

  const menuItems = [
    {
      title: "Documentos",
      description: "Gerenciar documentos",
      href: "/dashboard/documents",
      icon: FileText,
      color: "text-blue-600",
    },
    {
      title: "Busca",
      description: "Busca semântica",
      href: "/dashboard/search",
      icon: Search,
      color: "text-green-600",
    },
    {
      title: "Referências",
      description: "Gerenciar referências",
      href: "/dashboard/references",
      icon: BookOpen,
      color: "text-purple-600",
    },
    {
      title: "Projetos",
      description: "Gerenciar projetos",
      href: "/dashboard/projects",
      icon: FolderOpen,
      color: "text-orange-600",
    },
    {
      title: "Playbooks",
      description: "Gerenciar playbooks",
      href: "/dashboard/playbooks",
      icon: PlayCircle,
      color: "text-red-600",
    },
    {
      title: "Análises",
      description: "Gerenciar análises",
      href: "/dashboard/analyses",
      icon: FileText,
      color: "text-indigo-600",
    },
  ]

  return (
    <div className="container mx-auto py-10">
      <div className="mb-8">
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <p className="text-muted-foreground">Bem-vindo ao Banco de Referências</p>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {menuItems.map((item) => {
          const Icon = item.icon
          return (
            <Link
              key={item.href}
              href={item.href}
              className="group relative overflow-hidden rounded-lg border bg-card p-6 shadow-sm transition-all hover:shadow-md"
            >
              <div className="flex items-center gap-4">
                <div className={`rounded-lg bg-muted p-3 ${item.color}`}>
                  <Icon className="h-6 w-6" />
                </div>
                <div className="flex-1">
                  <h3 className="font-semibold">{item.title}</h3>
                  <p className="text-sm text-muted-foreground">{item.description}</p>
                </div>
              </div>
            </Link>
          )
        })}
      </div>
    </div>
  )
}

