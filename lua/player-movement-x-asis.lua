-- Add a new LocalScript "PlayerMovement" inside of StarterPlayer > StarterPlayerScripts

-- Services used for input, rendering, and player access
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local ContextActionService = game:GetService("ContextActionService")

local player = Players.LocalPlayer
local movementDirection = 0  -- -1 for left, 1 for right, 0 for no input

-- Handle custom input for left/right movement only
local function onAction(actionName, inputState, inputObj)
	if inputState == Enum.UserInputState.Begin then
		if actionName == "MoveLeft" then
			movementDirection = -1
		elseif actionName == "MoveRight" then
			movementDirection = 1
		end
	elseif inputState == Enum.UserInputState.End then
		-- Stop movement when input is released
		if actionName == "MoveLeft" or actionName == "MoveRight" then
			movementDirection = 0
		end
	end
	return Enum.ContextActionResult.Sink -- Block default behavior
end

-- Bind input keys (A/D or Arrow keys) to custom movement actions
ContextActionService:BindAction("MoveLeft", onAction, false, Enum.KeyCode.A, Enum.KeyCode.Left)
ContextActionService:BindAction("MoveRight", onAction, false, Enum.KeyCode.D, Enum.KeyCode.Right)

-- Apply movement every frame based on direction
RunService.RenderStepped:Connect(function(dt)
	local character = player.Character
	if character then
		local root = character:FindFirstChild("HumanoidRootPart")
		local humanoid = character:FindFirstChildOfClass("Humanoid")
		if root and humanoid then
			-- Move character along the X-axis only
			local moveVector = Vector3.new(movementDirection, 0, 0)
			humanoid:Move(moveVector, true)

			-- Flip character to face the direction they're moving
			if movementDirection ~= 0 then
				root.CFrame = CFrame.new(root.Position, root.Position + Vector3.new(movementDirection, 0, 0))
			end
		end
	end
end)
